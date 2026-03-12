# Intentional Data Quality Issues in `sample_data_with_errors.csv`

| # | Row(s) | Column | Error Type | Description |
|---|--------|--------|-----------|-------------|
| 1 | 3 | `email` | **Missing value** | Email is empty |
| 2 | 7 | `score` | **Missing value** | Score is empty |
| 3 | 9 | `phone` | **Missing value** | Phone number is empty |
| 4 | 4 | `salary` | **NULL string** | Salary contains literal text `NULL` instead of a numeric value |
| 5 | 24 | `date_of_birth` | **NULL string** | Date of birth contains literal `NULL` |
| 6 | 2 | `date_of_birth` | **Inconsistent date format** | Uses `DD.MM.YYYY` instead of `YYYY-MM-DD` |
| 7 | 15 | `date_of_birth` | **Inconsistent date format** | Uses `MM/DD/YYYY` |
| 8 | 6 | `registration_date` | **Inconsistent date format** | Uses `DD-MM-YYYY` instead of `YYYY-MM-DD` |
| 9 | 19 | `registration_date` | **Ambiguous date format** | Uses `YY-MM-DD` (2-digit year) |
| 10 | 6 | `date_of_birth` | **Invalid date** | Month 13 does not exist (`1988-13-05`) |
| 11 | 5 | `date_of_birth` | **Invalid date** | 2000-02-29 — 2000 is a leap year so technically valid, but worth flagging for review |
| 12 | 30 | `date_of_birth` | **Unrealistic date** | Birth year `2099` is in the future |
| 13 | 7 | `name` | **Separator inside field** | Name `Müller; Hans` contains a semicolon, shifting all subsequent columns → row has 12 apparent columns |
| 14 | 22 | (end) | **Extra column** | Row has an extra `extra_field` value at the end (12 fields instead of 11) |
| 15 | 23 | `score` | **Missing column** | Row has only 10 fields — `score` column is absent |
| 16 | 11–12 | all | **Duplicate row** | Row id 11 (Marco Richter) appears twice identically |
| 17 | 5 | `email` | **Invalid email** | `thomas.fischer` — missing `@domain` |
| 18 | 25 | `email` | **Invalid email** | `tim schulze@@example.com` — double `@@` and space in local part |
| 19 | 8 | `salary` | **Negative value** | Salary is `-32000.00` (unrealistic) |
| 20 | 13 | `salary` | **Outlier value** | Salary `999999.99` is an extreme outlier |
| 21 | 27 | `salary` | **Suspicious zero** | Salary is `0.00` |
| 22 | 16 | `salary` | **Unit in numeric field** | `47000 EUR` — contains text in a numeric column |
| 23 | 10 | `salary` | **Wrong decimal separator** | Uses comma: `54000,50` instead of `54000.50` |
| 24 | 29 | `salary` | **Wrong thousand/decimal separator** | `48,500.00` — ambiguous comma usage |
| 25 | 21 | `salary` | **Leading whitespace** | `  65000.00` has leading spaces |
| 26 | 5 | `is_active` | **Inconsistent boolean** | `yes` instead of `true/false` |
| 27 | 10 | `is_active` | **Inconsistent boolean** | `TRUE` (different casing) |
| 28 | 12 | `is_active` | **Inconsistent boolean** | `0` instead of `true/false` |
| 29 | 18 | `is_active` | **Invalid boolean** | `maybe` is not a valid boolean |
| 30 | 13 | `score` | **Out-of-range value** | Score `101.3` exceeds plausible 0–100 range |
| 31 | 12 | `score` | **Negative score** | Score `-5.0` is below plausible range |
| 32 | 17 | `score` | **Non-numeric value** | `N/A` in a numeric column |
| 33 | 21 | `score` | **Non-numeric value** | `NaN` in a numeric column |
| 34 | 28 | `score` | **Non-numeric value** | `PASS` (categorical text in numeric column) |
| 35 | 26 | `department` | **Inconsistent category** | `Marketing Department` instead of `Marketing` |
| 36 | 27 | `phone` | **Invalid phone format** | `12345` — too short, no country code |
| 37 | 15 | `phone` | **Inconsistent phone format** | `0174-333-0665` — uses dashes, no `+49` prefix |
| 38 | 22 & 16 | `id` | **Duplicate primary key** | id = 14 which is already used before |
| 39 | 27 | `name` | **Separator inside field** | Name `Schulze; Tim` contains a semicolon and this time the csv contains all other columns |

**Total: 39 intentional data quality issues** across missing values, type mismatches, format inconsistencies, NULL literals, separator conflicts, duplicates, structural errors, outliers, duplicate primary keys and invalid entries.
