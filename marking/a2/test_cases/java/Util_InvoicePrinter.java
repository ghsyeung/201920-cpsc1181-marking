public class Util_InvoicePrinter {
  private static double roundUnitPrice(double r) {
    return Math.round(r * 100) / 100.0;
  }

  public static void print(Invoice invoice) {
    System.out.println("Total number of Products: " + invoice.getTotalOfLineItems());
    System.out.println("Total Quantity: " + invoice.getTotalQuantity());
    System.out.println("Total Price: " + roundUnitPrice(invoice.getTotalPrice()));
    System.out.println("Total Tax: " + roundUnitPrice(invoice.getTotalTax()));
  }
}
