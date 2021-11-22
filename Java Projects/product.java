public class product{
    private String name;
    private double price;
    private double discount;
    private String location;
    private int quantity;

    public product(){
        name = "None";
        price = 0.0;
        discount = 0.0;
        location = "None";
        quantity = 0;
    }
    public product(String objname, double objprice, double objdiscount, String objLocation, int objQuantity){
        name = objname;
        price = objprice;
        discount = objdiscount;
        location = objLocation;
        quantity = objQuantity;
    }
    public String getName(){
        return name;
    }
    public double getPrice(){
        return price;
    }
    public double getDiscount(){
        return discount;
    }
    public String getLocation(){
        return location;
    }
    public int getQuantity(){
        return quantity;
    }
    public void setPrice(double price){
        this.price = price;
    }
    public void setDiscount(double discount){
        this.discount = discount;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setLocation(String location){
        this.location = location;
    }
    public void setQuantity(int quantity){
        this.quantity = quantity;
    }
    public void printProduct(){
        System.out.println("Product Name: " + name);
        System.out.print("Price: $");
        System.out.printf("%.2f", price);
        System.out.println();
        System.out.print("Available Discount: ");
        System.out.printf("%.2f", (discount * 100));
        System.out.println("%");
        System.out.println("Location of Product: " + location);
        System.out.println("Quantity available in stock: " + quantity);
        System.out.println();
    }
}