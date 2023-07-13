import os

from pathlib import Path

from cffi import FFI
ffibuilder = FFI()

cpp_path = Path("cpp") / "spake2-c"

sources = []
sources.append(str(cpp_path / "sha512.c"))
sources.append(str(cpp_path / "spake2.c"))

include_dirs = []
include_dirs.append(str(cpp_path / "include"))
include_dirs.append(str(cpp_path))

ffibuilder.set_source(
    "_spake2_cffi",
    """
    #include "spake2/spake2.h"
    """,
    include_dirs=include_dirs,
    sources=sources,
)

ffibuilder.cdef("""
#define SPAKE2_MAX_MSG_SIZE 32
#define SPAKE2_MAX_KEY_SIZE 64

enum spake2_role_t {
  spake2_role_alice,
  spake2_role_bob,
};

enum spake2_state_t {
  spake2_state_init = 0,
  spake2_state_msg_generated,
  spake2_state_key_generated,
};

struct spake2_ctx_st {
  uint8_t private_key[32];
  uint8_t my_msg[32];
  uint8_t password_scalar[32];
  uint8_t password_hash[64];
  uint8_t *my_name;
  size_t my_name_len;
  uint8_t *their_name;
  size_t their_name_len;
  enum spake2_role_t my_role;
  enum spake2_state_t state;
  char disable_password_scalar_hack;
};

extern struct spake2_ctx_st *SPAKE2_CTX_new(enum spake2_role_t my_role,
				    const uint8_t *my_name, size_t my_name_len,
				    const uint8_t *their_name, size_t their_name_len);

extern void SPAKE2_CTX_free(struct spake2_ctx_st *ctx);

extern int SPAKE2_generate_msg(struct spake2_ctx_st *ctx,
				    uint8_t *out, size_t *out_len, size_t max_out_len,
                    const uint8_t *password, size_t password_len);

extern int SPAKE2_process_msg(struct spake2_ctx_st *ctx,
				    uint8_t *out_key, size_t *out_key_len,
                    size_t max_out_key_len, const uint8_t *their_msg,
                    size_t their_msg_len);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)