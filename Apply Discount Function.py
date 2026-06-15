def apply_discount(price, discount):
    # 1. Check if price is a number
    if not isinstance(price, (int, float)):
        return 'The price should be a number.'
    
    # 2. Check if the discount is a number
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number.'
        
    # 3. Check if the price is 0 or less
    if price <= 0:
        return 'The price should be greater than 0.'
        
    # 4. Check if the discount is out of bounds
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100.'
    
    # 5. Calculate and return the final price
    return price * (1 - discount / 100)
