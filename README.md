# Для работы необходимо создать фаил  .env

Этот файл содержит настройки для конфигурации программы парсинга данных.

## Переменные конфигурации

### USER_LOGIN
Укажите логин для доступа к ресурсу. Оставьте поле пустым, если логин не требуется.

### USER_PASSWORD
Укажите пароль для доступа к ресурсу. Оставьте поле пустым, если пароль не требуется.

### BRENDS
Список брендов и количество страниц, которые необходимо парсить. Укажите данные в формате:
Пример:BRENDS=hiwatch=11, hikvision=170, ezviz=5, ruijie=14, hikmicro=8, volta=6, uniview=1, umbrella=1, seagate=1, western_digital=1

#### Описание полей:
- **hiwatch**: количество страниц для бренда HiWatch (например, 11).
- **hikvision**: количество страниц для бренда Hikvision (например, 170).
- **ezviz**: количество страниц для бренда EZVIZ (например, 5).
- **ruijie**: количество страниц для бренда Ruijie (например, 14).
- **hikmicro**: количество страниц для бренда Hikmicro (например, 8).
- **volta**: количество страниц для бренда Volta (например, 6).
- **uniview**: количество страниц для бренда Uniview (например, 1).
- **umbrella**: количество страниц для бренда Umbrella (например, 1).
- **seagate**: количество страниц для бренда Seagate (например, 1).
- **western_digital**: количество страниц для бренда Western Digital (например, 1).

## Как использовать

1. Заполните необходимые поля `USER_LOGIN` и `USER_PASSWORD`, если требуется авторизация.
2. Укажите бренды и количество страниц для парсинга в переменной `BRENDS` в указанном формате.
3. Сохраните изменения и запустите программу.
