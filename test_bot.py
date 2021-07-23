from image_sharing import ImageSharing
import pytest
import asyncio
class MockView:
    def __init__(self, args):
        self.index = 1
        self.args = args
    def skip_ws(self):
        pass
    def eof(self):
        if self.ind > len(self.args):
            print("eof")
            return True
        return False
class MockBot:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
        self.can_run = self.return_true
        self.command = None
        self.bot = self
        self.view = MockView(self.args)
        self.init = True
        self.ind = 0
    def __setattr__(self, name: str, value) -> None:
        try:
            if name == "args" or name == "kwargs" and self.init:
                print(f"Potential Bug! {name} should not be changed! (current value: {getattr(self, name)})")
        except:
            pass
        super().__setattr__(name, value)
    async def return_true(self, *args, **kwargs):
        return True
    def sync_return_true(self, *args, **kwargs):
        return True
    async def send(self, *args, **kwargs):
        print(f"Would send message with args: {args} and kwargs: {kwargs}")
class CogTestClient:
    def __init__(self, cog):
        self._cog = cog(MockBot(None, None))
    def run_command(self, command, *args, **kwargs):
        pass_args = list(args)
        pass_args.insert(0, self._cog)
        pass_args.insert(1, MockBot(args, kwargs))
        print(pass_args)
        asyncio.run(getattr(self._cog, command)(*pass_args, **kwargs))

@pytest.fixture
def client():
    yield CogTestClient(ImageSharing)

def test_allmemes(client):
    client.run_command("allmemes")