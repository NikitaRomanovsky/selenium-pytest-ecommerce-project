from selenium.webdriver.common.by import By


class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (
        By.CSS_SELECTOR,
        "tr.wc-block-cart-items__row .wc-block-cart-item__product .wc-block-components-product-name",
    )

    EXPAND_COUPON_INPUT_BUTTON = (
        By.CSS_SELECTOR,
        ".wp-block-woocommerce-cart-order-summary-coupon-form-block",
    )

    COUPON_CODE_INPUT_FIELD = (By.ID, "wc-block-components-totals-coupon__input-coupon")

    APPLY_COUPON_CODE_BUTTON = (
        By.CSS_SELECTOR,
        'button[class*="wc-block-components-totals-coupon__button"]',
    )

    COUPON_CODE_APPLIED_POP_UP = (
        By.CSS_SELECTOR,
        ".wc-block-components-notices__snackbar",
    )

    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".wc-block-cart__submit")

    TOTAL_MONEY_AMMOUNT = (
        By.CSS_SELECTOR,
        ".wc-block-components-totals-item.wc-block-components-totals-footer-item .wc-block-formatted-money-amount",
    )
