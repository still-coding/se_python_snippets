from config import DATABASE_URI
from model import Customer, Order, OrderDetails, Product
from tools import get_session_engine
from sqlalchemy import select, func

def execute_query(session, query, print_results=False):
    results = session().execute(query).all()
    if print_results:
        for result in results:
            print(result)
        print('\n')
    return results


if __name__ == '__main__':
    sess, _ = get_session_engine(DATABASE_URI)
    all_customers = select(Customer)
    execute_query(sess, all_customers, print_results=True)
    
    orders = select(Order, Customer).join(Order.customer)
    execute_query(sess, orders, print_results=True)

    all_details = select(Order, Product, OrderDetails.quantity) \
        .join(OrderDetails, Order.id == OrderDetails.order_id) \
        .join(Product, OrderDetails.product_id == Product.id)
    execute_query(sess, all_details, print_results=True)

    orders_total = select(Order, func.sum(Product.price * OrderDetails.quantity)) \
        .join(OrderDetails, Order.id == OrderDetails.order_id) \
        .join(Product, OrderDetails.product_id == Product.id) \
        .group_by(Order.id).order_by(Order.id)
    results = execute_query(sess, orders_total, print_results=True)

    print('First order total queried:', results[0][1])

    first_order_query = select(Order).where(Order.id == 1)
    result = execute_query(sess, first_order_query)
    first_order = result[0][0]

    check_total = 0
    for details in first_order.details:
        check_total += details.product.price * details.quantity 
    print('First order total checked:', check_total)