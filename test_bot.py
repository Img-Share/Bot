from image_sharing import ImageSharing
import pytest
import asyncio

class MockBot:
    def __init__(self, args, kwargs):
        self.rargs = args
        self.rkwargs = kwargs
        self.can_run = self.return_true
        self.command = None
    def __getattribute__(self, name: str):
        if name == "dummy_callable":
            print("dummycallable got")
            return super().__getattribute__("dummy_callable")
        elif name in ["bot", "view", "ctx"]:
            return self
        elif name == "can_run":
            return self.return_true
        elif name == "eof":
            return None
        elif name == "args":
            return self.rargs
        elif name == "kwargs":
            return self.rkwargs
        elif name == "rargs":
            return super().__getattribute__("rargs")
        elif name == "rkwargs":
            return super().__getattribute__("rkwargs")
        elif name == "send":
            print("Send")
            return self.return_true
        elif name == "transform":
            print("Transform")
            print("ret arg return callable")
            return self.return_args_please_and_thank_you
        raise Exception(f"Tried to get {name} and fell through")

    def __setattr__(self, name: str, value) -> None:
        print(f"[mock] Tried to set {name} to {value}")
        super().__setattr__(name, value)
    async def return_true(self, *args, **kwargs):
        return True
    def sync_return_true(self, *args, **kwargs):
        return True
class CogTestClient:
    def __init__(self, cog):
        self._cog = cog(MockBot(None, None))
    def run_command(self, command, *args, **kwargs):
        pass_args = list(args[1:])
        pass_args.insert(0, MockBot(args, kwargs))
        print(pass_args)
        asyncio.run(getattr(self._cog, command).invoke(MockBot(pass_args, kwargs)))

@pytest.fixture
def client():
    yield CogTestClient(ImageSharing)

def test_allmemes(client):
    client.run_command("allmemes")