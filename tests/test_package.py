"""Smoke tests for the QuantEdge package."""

import quant_edge


def test_package_import() -> None:
    """Verify that the QuantEdge package can be imported."""
    assert quant_edge is not None
