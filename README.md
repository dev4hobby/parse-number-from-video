# Parse numeric character from video

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

![parse-number-from-area](./docs/images/parse-number-from-area.gif)

```bash
python parse_number_from_area.py
```

Parse number from all area w/ pytesseract
