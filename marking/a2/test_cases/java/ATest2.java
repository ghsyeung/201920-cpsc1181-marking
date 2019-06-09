public class ATest2 {
    public static void main(String[] args) {
        TaxCalculator taxCalculator = new TaxCalculator();
        InvoiceCalculator invoiceCalculator = new InvoiceCalculator(taxCalculator);
        OrderPrinter orderPrinter = new OrderPrinter();

        Order order1 = new Order();
        order1.addLineItem("Lord of the Rings", 30, 20.5);
        order1.addLineItem("Bible", 5, 5);
        order1.removeLineItem("Harry Potter");
        order1.addLineItem("Lord of the Rings", 22.5);
        order1.addLineItem("Harry Potter", 3, 10);

        orderPrinter.print(order1);

        Invoice invoice = invoiceCalculator.generateInvoice(order1);
        Util_InvoicePrinter.print(invoice);
    }
}
