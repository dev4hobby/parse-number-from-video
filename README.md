# Parse numeric character from video

## Requirements

```bash
# Install Tesseract
brew install tesseract
# Optional (Language pack)
brew install tesseract-lang 

# Install pytesseract package
pip install pytesseract
```


## Target video

![full-screen-image](./docs/images/full-screen.png)

## Step 1

![crop-only-number-area](./docs/images/cropped-number-area.png)

```python
python crop_number_area.py
```

Crop target area

> minimize the noise

## Step 2

![numbers-area](./docs/images/numbers-area.gif)

```bash
python get_numbers_area.py
```

Get all numbers area

## Step 3

![parse-numbe](./docs/images/parse-number.gif)

```bash
python parse_number_from_area.py
```

Parse number from all area w/ pytesseract
