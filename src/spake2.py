from _spake2 import lib, ffi

class Spake2:
    Alice = lib.spake2_role_alice
    Bob = lib.spake2_role_bob

    def __init__(self, my_role, my_name, their_name):
        self._ctx = None
        my_name = my_name + b'\0'
        their_name = their_name + b'\0'

        _my_name = ffi.new("uint8_t[]", my_name)
        _their_name = ffi.new("uint8_t[]", their_name)
        self._ctx = lib.SPAKE2_CTX_new(my_role, _my_name, len(my_name), _their_name, len(their_name))

    def generate_message(self, password):
        _out_msg = ffi.new("uint8_t[]", lib.SPAKE2_MAX_MSG_SIZE)
        _out_msg_len = ffi.new("size_t *")
        _out_msg_len[0] = 0
        _password = ffi.new("uint8_t[]", password)

        ret = lib.SPAKE2_generate_msg(self._ctx, _out_msg, _out_msg_len, lib.SPAKE2_MAX_MSG_SIZE, _password, len(password))
        out_msg_len = ffi.unpack(_out_msg_len, 1)[0]
        if ret == 0 or out_msg_len == 0:
            raise Exception('generate_msg error')
        out_msg = ffi.unpack(_out_msg, out_msg_len)
        return bytes(out_msg)
    
    def process_msg(self, their_msg):
        _out_key = ffi.new("uint8_t[]", lib.SPAKE2_MAX_KEY_SIZE)
        _out_key_len = ffi.new("size_t *")
        _out_key_len[0] = 0
        _their_msg = ffi.new("uint8_t[]", their_msg)

        ret = lib.SPAKE2_process_msg(self._ctx, _out_key, _out_key_len, lib.SPAKE2_MAX_KEY_SIZE, _their_msg, len(their_msg))
        out_key_len = ffi.unpack(_out_key_len, 1)[0]
        if ret == 0 or out_key_len == 0:
            raise Exception('process_msg error', ret, ffi.unpack(_out_key_len, 1)[0])
        out_key = ffi.unpack(_out_key, out_key_len)
        return bytes(out_key)

    def __del__(self):
        if self._ctx:
            lib.SPAKE2_CTX_free(self._ctx)

class Spake2_Alice(Spake2):
    def __init__(self, my_name, their_name):
        super().__init__(Spake2.Alice, my_name, their_name)

class Spake2_Bob(Spake2):
    def __init__(self, my_name, their_name):
        super().__init__(Spake2.Bob, my_name, their_name)