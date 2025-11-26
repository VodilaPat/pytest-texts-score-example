from pytest_texts_score_example import generate_response

from pytest_texts_score import texts_expect_f1_equal

### Basic test
def test_generate_response_basic():
    """Test standard input string."""
    input_text = "Hello world"
    expected = "AI said: Hello world"
    assert generate_response(input_text) == expected


def test_generated_good_response():
    input_text = "Life is short."
    expected = generate_response(input_text)
    texts_expect_f1_equal(input_text, expected,1,0.5)