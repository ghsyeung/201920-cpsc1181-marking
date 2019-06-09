public class ATest2_1 {
  public static void main(String[] args) {
    TaxCalculator taxCalculator = new TaxCalculator();
    InvoiceCalculator invoiceCalculator = new InvoiceCalculator(taxCalculator);
    OrderPrinter orderPrinter = new OrderPrinter();

    Order order1 = new Order();
    orderPrinter.print(order1);

    Invoice invoice = invoiceCalculator.generateInvoice(order1);
    Util_InvoicePrinter.print(invoice);
  }
}
