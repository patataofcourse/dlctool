from pyctr.crypto.engine import CryptoEngine, Keyslot

def test_open_crypto(f, tid, name, key=(b"\0"*16)):
    global engine
    engine = CryptoEngine()
    engine.setup_sd_key(key)
    path = "/title/0004008c/%08x/content/00000000/%s" % (tid % (1 << 32), name)
    print(path)
    return engine.create_ctr_io(Keyslot.SD, f, engine.sd_path_to_iv(path))