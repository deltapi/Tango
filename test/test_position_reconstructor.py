from src.map.position import Position
from src.map.position_reconstructor import reconstructPosition


def test_reconstruct_position_only_forward():
    newPosition = reconstructPosition(0, 0, Position(0, 0), 100)
    print(newPosition)


def test_reconstruct_position_only_sideways():
    newPosition = reconstructPosition(0, 90, Position(0, 0), 100)
    print(newPosition)

test_reconstruct_position_only_sideways()
