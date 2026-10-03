# main.py
# Коммит 1: док: добавить мини-ТЗ для калькулятора скидок — только README.md с ТЗ.
# Коммит 2: функ: реализовать калькулятор скидок — этот файл с логикой расчёта.

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def calculate_discount(price: Decimal, discount_percent: Decimal) -> tuple[Decimal, Decimal]:
    """Возвращает сумму скидки и итоговую цену."""
    if price <= 0:
        raise ValueError("Цена должна быть больше 0")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100")

    discount_amount = (price * discount_percent / Decimal("100")).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    final_price = (price - discount_amount).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return discount_amount, final_price


def main() -> None:
    try:
        price = Decimal(input("Введите цену: ").replace(",", "."))
        discount_percent = Decimal(input("Введите процент скидки: ").replace(",", "."))

        discount_amount, final_price = calculate_discount(price, discount_percent)

        print(f"Сумма скидки: {discount_amount}")
        print(f"Итоговая цена: {final_price}")
    except (InvalidOperation, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
