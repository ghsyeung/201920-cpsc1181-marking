public class ATest1_1 {
    public static void main(String[] args) {
        Order order1 = new Order();

        order1.addLineItem("Bible", 50, 5);
        order1.addLineItem("Bible", 20, 5);
        order1.addLineItem("Bible", 50, 1);
        order1.addLineItem("Bible", 10, 500);
        order1.removeLineItem("Harry Potter");

        OrderPrinter orderPrinter = new OrderPrinter();

        orderPrinter.print(order1);
    }
}
