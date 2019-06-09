public class ATestBonus_1 {
  public static void main(String[] args) {
    TaxCalculator taxCalculator = new TaxCalculator();
    InvoiceCalculator invoiceCalculator = new InvoiceCalculator(taxCalculator);
    OrderPrinter orderPrinter = new OrderPrinter();

    Order order1 = new Order();

    InvoicePrinter ip = new InvoicePrinter();
    CheckoutService cs = new CheckoutService(invoiceCalculator, orderPrinter, ip);
    cs.checkout(order1);
  }
}
