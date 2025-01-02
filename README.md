# FuzzyDishwasher
This project aims to simulate dishwasher with fuzzy logic.
---

**Usage**

<pre>
  https://github.com/CountZero-Error/FuzzyDishwasher.git
  cd FuzzyDishwasher/
  pip install scikit-fuzzy numpy
  python dishwasher.py
</pre>

---

## TABLE OF CONTENT
### $~~~~~$ - Inputs
### $~~~~~$ - Outputs
### $~~~~~$ - Fuzzy Mapping Table

---

## **Inputs**

**3 required inputs:**
1) **Dirtiness Level**
2) **Dish Quantity**
3) **Water Hardness**

#### **1. Dirtiness Level**
- **Description**: How dirty the dishes are.
- **Range**: 0 (clean) to 5 (extremely dirty).
- **Linguistic Terms**:
  - **Low**: Lightly soiled dishes (e.g., dust or minor food stains).
  - **Medium**: Moderately dirty dishes (e.g., dried sauces or mild grease).
  - **High**: Heavily soiled dishes (e.g., burnt food or heavy grease).

![clipboard](https://github.com/user-attachments/assets/f2a28d7d-6046-452a-85cd-3725144d7335)

#### **2. Dish Quantity**
- **Description**: Number of dishes loaded into the dishwasher.
- **Range**: 0 (no dishes) to 10 (maximum capacity).
- **Linguistic Terms**:
  - **Few**: Less than one-third of the dishwasher is loaded.
  - **Moderate**: Between one-third and two-thirds loaded.
  - **Many**: More than two-thirds loaded.
    
![clipboard1](https://github.com/user-attachments/assets/c3613b86-6466-42c7-b9e9-84dce9913cdf)

#### **3. Water Hardness**
- **Description**: The hardness of the water being used.
- **Range**: 0 (soft water) to 10 (very hard water).
- **Linguistic Terms**:
  - **Soft**: Little or no hardness.
  - **Moderate**: Medium mineral content.
  - **Hard**: High mineral content, requiring more detergent.

![clipboard2](https://github.com/user-attachments/assets/58309794-dbde-4039-ba5b-062dd2972e17)

---
## **Outputs**

**3 outputs:**
1) **Wash Time**
2) **Detergent Amount**
3) **Water Temperature**

#### **1. Wash Time**
- **Description**: The duration of the washing cycle.
- **Range**: 0 to 60 minutes.
- **Linguistic Terms**:
  - **Short**: Quick rinse or lightly soiled dishes (0–20 minutes).
  - **Medium**: Moderate wash time for normal loads (15–40 minutes).
  - **Long**: Extended wash for very dirty dishes or heavy loads (30–60 minutes).

![clipboard6](https://github.com/user-attachments/assets/5a662a54-bd11-444f-9229-7c4489173283)

#### **2. Detergent Amount**
- **Description**: The quantity of detergent to use.
- **Range**: 0 (none) to 10 (maximum dosage).
- **Linguistic Terms**:
  - **Low**: Minimal detergent (0–3 units).
  - **Medium**: Moderate detergent for average loads (3–7 units).
  - **High**: High detergent for heavy loads or very dirty dishes (7–10 units).

![clipboard3](https://github.com/user-attachments/assets/659e995e-fabc-4f6d-b1c5-d65ac0c988b1)

#### **3. Water Temperature**
- **Description**: The temperature of the water during the washing cycle.
- **Range**: 30°C to 90°C.
- **Linguistic Terms**:
  - **Low**: Warm water for delicate loads or lightly soiled dishes (30–50°C).
  - **Medium**: Hot water for normal cleaning (50–70°C).
  - **High**: Very hot water for heavy cleaning (70–90°C).

![clipboard9](https://github.com/user-attachments/assets/61bbf453-9e58-466f-b5f4-785b15877edc)

---
## **Fuzzy Mapping Table**

**Inputs:** **Dirtiness Level**, **Dish Quantity**, **Water Hardness**

**Outputs:** **Wash Time**, **Detergent Amount**, **Water Temperature**

| **Dirtiness Level** | **Dish Quantity** | **Water Hardness** | **Wash Time** | **Detergent Amount** | **Water Temperature** |
|---------------------|-------------------|--------------------|---------------|----------------------|-----------------------|
| Low                 | Few              | Soft               | Short         | Low                  | Low                   |
| Low                 | Few              | Moderate           | Short         | Low                  | Medium                |
| Low                 | Few              | Hard               | Medium        | Medium               | Medium                |
| Low                 | Moderate         | Soft               | Short         | Low                  | Medium                |
| Low                 | Moderate         | Moderate           | Medium        | Medium               | Medium                |
| Low                 | Moderate         | Hard               | Medium        | Medium               | Medium                |
| Low                 | Many             | Soft               | Medium        | Medium               | Medium                |
| Low                 | Many             | Moderate           | Medium        | Medium               | Medium                |
| Low                 | Many             | Hard               | Medium        | Medium               | Medium                |
| Medium              | Few              | Soft               | Medium        | Low                  | Medium                |
| Medium              | Few              | Moderate           | Medium        | Medium               | Medium                |
| Medium              | Few              | Hard               | Medium        | Medium               | Medium                |
| Medium              | Moderate         | Soft               | Medium        | Medium               | Medium                |
| Medium              | Moderate         | Moderate           | Medium        | Medium               | Medium                |
| Medium              | Moderate         | Hard               | Medium        | Medium               | Medium                |
| Medium              | Many             | Soft               | Long          | Medium               | High                  |
| Medium              | Many             | Moderate           | Long          | Medium               | High                  |
| Medium              | Many             | Hard               | Long          | Medium               | High                  |
| High                | Few              | Soft               | Medium        | Medium               | Medium                |
| High                | Few              | Moderate           | Medium        | Medium               | High                  |
| High                | Few              | Hard               | Medium        | Medium               | High                  |
| High                | Moderate         | Soft               | Medium        | High                 | Medium                |
| High                | Moderate         | Moderate           | Long          | High                 | High                  |
| High                | Moderate         | Hard               | Long          | High                 | High                  |
| High                | Many             | Soft               | Long          | High                 | High                  |
| High                | Many             | Moderate           | Long          | High                 | High                  |
| High                | Many             | Hard               | Long          | High                 | High                  |
