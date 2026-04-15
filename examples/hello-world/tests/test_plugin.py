"""
Tests für Hello World Plugin
"""

import pytest
import asyncio
from main import HelloWorldPlugin


@pytest.mark.asyncio
async def test_hello_world_default():
    """Test hello_world mit Standard-Parameter"""
    plugin = HelloWorldPlugin()
    result = await plugin.hello_world()

    assert result["success"] is True
    assert "World" in result["message"]
    assert result["call_count"] == 1


@pytest.mark.asyncio
async def test_hello_world_with_name():
    """Test hello_world mit custom Name"""
    plugin = HelloWorldPlugin()
    result = await plugin.hello_world("Alice")

    assert result["success"] is True
    assert "Alice" in result["message"]
    assert "Hello" in result["message"]


@pytest.mark.asyncio
async def test_hello_world_call_count():
    """Test dass call_count inkrementiert wird"""
    plugin = HelloWorldPlugin()

    # Erste Aktion
    result1 = await plugin.hello_world()
    assert result1["call_count"] == 1

    # Zweite Aktion
    result2 = await plugin.hello_world("Bob")
    assert result2["call_count"] == 2

    # Dritte Aktion
    result3 = await plugin.hello_world("Charlie")
    assert result3["call_count"] == 3


@pytest.mark.asyncio
async def test_count_to_n_default():
    """Test count_to_n mit Standard-Parameter"""
    plugin = HelloWorldPlugin()
    result = await plugin.count_to_n()

    assert result["success"] is True
    assert result["count"] == [1, 2, 3, 4, 5]
    assert result["total"] == 5
    assert result["sum"] == 15


@pytest.mark.asyncio
async def test_count_to_n_custom():
    """Test count_to_n mit custom Wert"""
    plugin = HelloWorldPlugin()
    result = await plugin.count_to_n(7)

    assert result["success"] is True
    assert result["count"] == [1, 2, 3, 4, 5, 6, 7]
    assert result["total"] == 7
    assert result["sum"] == 28


@pytest.mark.asyncio
async def test_count_to_n_invalid_negative():
    """Test dass negative Werte rejected werden"""
    plugin = HelloWorldPlugin()
    result = await plugin.count_to_n(-5)

    assert result["success"] is False
    assert "error" in result


@pytest.mark.asyncio
async def test_count_to_n_invalid_zero():
    """Test dass Null rejected wird"""
    plugin = HelloWorldPlugin()
    result = await plugin.count_to_n(0)

    assert result["success"] is False
    assert "error" in result


@pytest.mark.asyncio
async def test_count_to_n_invalid_too_large():
    """Test dass zu große Werte rejected werden"""
    plugin = HelloWorldPlugin()
    result = await plugin.count_to_n(200)

    assert result["success"] is False
    assert "error" in result
    assert "größer als 100" in result["error"]


def test_get_tools():
    """Test dass get_tools die korrekten Tools zurückgibt"""
    plugin = HelloWorldPlugin()
    tools = plugin.get_tools()

    assert len(tools) == 2
    assert "hello_world" in tools
    assert "count_to_n" in tools
    assert callable(tools["hello_world"])
    assert callable(tools["count_to_n"])


@pytest.mark.asyncio
async def test_plugin_without_kernel():
    """Test dass Plugin auch ohne Kernel funktioniert"""
    plugin = HelloWorldPlugin(kernel=None)
    result = await plugin.hello_world("Test")

    # Sollte nicht crashen
    assert result["success"] is True
