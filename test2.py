from localstack.services import infra

def setup():
    infra.start_infra(asynchronous=True)

def teardown():
    infra.stop_infra()

def my_app_test():
    # here goes your test logic

