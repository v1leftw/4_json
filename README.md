# Prettify JSON

Script outputs JSON-file in easy-to-read format

# Quickstart


Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
...
{
            "geometry": {
                "coordinates": [
                    37.77498232370723,
                    55.70337880867678
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "Волгоградский проспект, дом 106, корпус 1",
                    "AdmArea": "Юго-Восточный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Кузьминки",
                    "IsNetObject": "нет",
                    "Name": "Крафтовое пиво",
                    "OperatingCompany": null,
                    "PublicPhone": [
                        {
                            "PublicPhone": "нет телефона"
                        }
                    ],
                    "TypeService": "реализация продовольственных товаров",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "вторник",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "среда",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "четверг",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "пятница",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "суббота",
                            "Hours": "09:00-23:00"
                        },
                        {
                            "DayOfWeek": "воскресенье",
                            "Hours": "09:00-23:00"
                        }
                    ],
                    "global_id": 171714335
                },
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "RowId": "edc22bd8-0d2c-456d-b754-b8cef098f5d5",
                "VersionNumber": 1
            },
            "type": "Feature"
        },
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
