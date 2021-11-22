import java.util.Scanner;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Random;

public class Main {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        String username;
        String password;
        boolean correctAccount;
        String command;
        ArrayList<product> Inventory = new ArrayList<product>();
        String nameObj;
        double priceObj = 0.0;
        double discountObj = 0.0;
        String removeObj;
        String locationObj;
        int quantityObj;
        String nameToCompare;
        Location match;
        String objectToPay;
        int numItemsToPay;
        product updateQuantity;
        ArrayList<product> purchaseList = new ArrayList<product>();
        ArrayList<Integer> listOfNumItemsToPay = new ArrayList<Integer>();
        Random randomNum = new Random();
        int numOfBags;
        double taxValue = 0.07;
        double bagValue = 0.25;
        
        do{
            System.out.println("Please insert your username:");
            username = scnr.nextLine();
            System.out.println("Please insert your password:");
            password = scnr.nextLine();
            correctAccount = AccountCheck.correctAccount(username, password);

            if(correctAccount){
                System.out.println("Welcome Joel");
            }
            else{
                System.out.println("Access Denied");
                System.out.println("Try Again");
            }
        }while(!correctAccount);

        System.out.println("Commands:");
        System.out.println("'i' = Inventory");
        System.out.println("'p' = Payment");
        System.out.println("'s' = Settings");
        System.out.println("'q' = Exit");
            
        command = scnr.next();
        if((command.charAt(0) == 'q') && (command.length() == 1)){

        }
        else{                            
            do{
                if((command.charAt(0) == 'i') && (command.length() == 1)){
                    do{
                        System.out.println("Subcommands for Inventory:");
                        System.out.println("'a' = Add things to the Inventory");
                        System.out.println("'r' = Remove things from the Inventory");
                        System.out.println("'s' = Show items in Inventory");
                        System.out.println("'e' = Edit Inventory");
                        System.out.println("'q' = Exit Inventory section");
                        command = scnr.next();                           
                        if((command.charAt(0) == 'a') && (command.length() == 1)){
                            do{
                                scnr.nextLine();
                                System.out.println("Type the name of the new object:");
                                nameObj = scnr.nextLine();
                                System.out.println("Type the price in decimals");
                                try{
                                    if(scnr.hasNextDouble()){
                                        priceObj = scnr.nextDouble();
                                    }
                                    else{
                                        priceObj = 0.0;
                                        throw new InputMismatchException("Invalid input");
                                    }
                                    System.out.println("Is there are discount for this new object? Type the discount in decimals (ex. 0.20) even if it's zero");
                                    if(scnr.hasNextDouble()){    
                                        discountObj = scnr.nextDouble();
                                    }
                                    else{
                                        discountObj = 0.0;
                                        scnr.nextLine();
                                        throw new InputMismatchException("Invalid input");
                                    }
                                    scnr.nextLine();
                                    System.out.println("In which aisle is the product going to be located?");
                                    locationObj = scnr.nextLine();
                                    System.out.println("How many products are there currently?");
                                    if(scnr.hasNextInt()){
                                        quantityObj = scnr.nextInt();
                                    }
                                    else{
                                        scnr.nextLine();
                                        throw new InputMismatchException("Invalid input");
                                    }
                                    product newObject = new product(nameObj, priceObj, discountObj, locationObj, quantityObj);
                                    addProduct(newObject, Inventory);
                                }
                                catch(InputMismatchException expt){
                                    System.out.println(expt.getMessage());
                                }
                                do{
                                    scnr.nextLine();
                                    System.out.println("Would you like to add another product? Type 'n' for no and 'y' for yes");
                                    command = scnr.next();
                                    if((command.charAt(0) == 'n') && (command.length() == 1) || (command.charAt(0) == 'y') && (command.length() == 1)){
                                        break;
                                    }
                                    else{
                                        System.out.println("Invalid command");
                                    }
                                }while((command.length() != 1) || (command.charAt(0) != 'n'));
                            }while(command.charAt(0) != 'n');
                        }
                        else if((command.charAt(0) == 'r') && (command.length() == 1)){
                            do{
                                scnr.nextLine();
                                try{
                                    System.out.println("Type the name of the product you want to remove from the Inventory:");
                                    removeObj = scnr.nextLine();
                                    match = checkInventory(removeObj, Inventory);
                                    if(match.getMatch()){
                                        removeProduct(removeObj, Inventory);
                                    }
                                    else{
                                        throw new InputMismatchException("Error: Couldn't find object in Inventory");
                                    }
                                }
                                catch(InputMismatchException expt){
                                    System.out.println(expt.getMessage());
                                }
                                do{
                                    scnr.nextLine();
                                    System.out.println("Would you like to remove another product from Inventory? Type 'n' for no and 'y' for yes");
                                    command = scnr.next();
                                    if((command.charAt(0) == 'n') && (command.length() == 1) || (command.charAt(0) == 'y') && (command.length() == 1)){
                                        break;
                                    }
                                    else{
                                        System.out.println("Invalid command");
                                    }
                                }while((command.length() != 1) || (command.charAt(0) != 'n'));
                            }while(command.charAt(0) != 'n');
                        }
                        else if((command.charAt(0) == 's') && (command.length() == 1)){
                            showInventory(Inventory);
                        }
                        else if((command.charAt(0) == 'e') && (command.length() == 1)){
                            if(Inventory.size() > 0){    
                                do{
                                    scnr.nextLine();
                                    System.out.println("Type the name of the product you would like to edit:");
                                    nameToCompare = scnr.nextLine();
                                    match = checkInventory(nameToCompare, Inventory);
                                    while(!match.getMatch()){
                                        System.out.println("Error: Cannot Find Item in Inventory");
                                        System.out.println("Try Again");
                                        System.out.println("Type the name of the product you would like to edit:");
                                        nameToCompare = scnr.nextLine();
                                        match = checkInventory(nameToCompare, Inventory);
                                    }
                                    System.out.println("Match found for item: " + nameToCompare);
                                    System.out.println("What would you like to edit for this product:");
                                    System.out.println("'n' = name");
                                    System.out.println("'p' = price");
                                    System.out.println("'d' = discount");
                                    System.out.println("'l' = location");
                                    System.out.println("'q' = quantity");
                                    command = scnr.next();
                                    if((command.charAt(0) == 'n') && (command.length() == 1)){
                                        scnr.nextLine();
                                        System.out.println("Type the new name of the product");
                                        nameObj = scnr.nextLine();
                                        editName(nameObj, Inventory, match);
                                    }
                                    else if((command.charAt(0) == 'p') && (command.length() == 1)){
                                        scnr.nextLine();
                                        System.out.println("Type the new price of the product");
                                        try{    
                                            if(scnr.hasNextDouble()){
                                                priceObj = scnr.nextDouble();
                                                editPrice(priceObj, Inventory, match);
                                            }
                                            else{
                                                throw new InputMismatchException("Invalid input");
                                            }
                                        }
                                        catch(InputMismatchException expt){
                                            System.out.println(expt.getMessage());
                                        }
                                    }
                                    else if((command.charAt(0) == 'd') && (command.length() == 1)){
                                        scnr.nextLine();
                                        System.out.println("Type the new discount of the product");
                                        try{
                                            if(scnr.hasNextDouble()){
                                                discountObj = scnr.nextDouble();
                                                editDiscount(discountObj, Inventory, match);
                                            }
                                            else{
                                                throw new InputMismatchException("Invalid input");
                                            }
                                        }
                                        catch(InputMismatchException expt){
                                            System.out.println(expt.getMessage());
                                        }
                                    }
                                    else if((command.charAt(0) == 'l') && (command.length() == 1)){
                                        scnr.nextLine();
                                        System.out.println("Type the new location for this product");
                                        locationObj = scnr.next();
                                        editLocation(locationObj, Inventory, match);
                                    }
                                    else if((command.charAt(0) == 'q') && (command.length() == 1)){
                                        scnr.nextLine();
                                        System.out.println("Type the new quantity available in stock");
                                        try{
                                            if(scnr.hasNextInt()){
                                                quantityObj = scnr.nextInt();
                                                editQuantity(quantityObj, Inventory, match);
                                            }
                                            else{
                                                throw new InputMismatchException("Invalid Input");
                                            }
                                        }
                                        catch(InputMismatchException expt){
                                            System.out.println(expt.getMessage());
                                        }
                                    }
                                    else{
                                        System.out.println("Invalid Command. Try again");
                                    }
                                    do{
                                        scnr.nextLine();
                                        System.out.println("Would you like to edit another product? Type 'n' for no and 'y' for yes");
                                        command = scnr.next();
                                        if((command.charAt(0) == 'n') && (command.length() == 1) || (command.charAt(0) == 'y') && (command.length() == 1)){
                                            break;
                                        }
                                        else{
                                            System.out.println("Invalid command");
                                        }
                                    }while((command.length() != 1) || (command.charAt(0) != 'n'));
                                }while(command.charAt(0) != 'n');
                            }
                            else{
                                System.out.println("There are no items in the Inventory");
                            }
                        }
                        else if((command.charAt(0) == 'q') && (command.length() == 1)){
                        }
                        else{
                            System.out.println("Invalid Command");
                        }
                    }while((command.charAt(0) != 'q') || command.length() != 1);
                }
                else if((command.charAt(0) == 'p') && (command.length() == 1)){
                    if(Inventory.size() > 0){
                        do{
                            scnr.nextLine();
                            System.out.println("Type name of product to purchase");
                            objectToPay = scnr.nextLine();
                            System.out.println("Type how many of such product are going to be purchased");
                            try{
                                if(scnr.hasNextInt()){
                                    numItemsToPay = scnr.nextInt();
                                    match = checkInventory(objectToPay, Inventory);
                                    if(match.getMatch()){
                                        purchaseList.add(Inventory.get(match.getMatchIndex()));
                                        updateQuantity = Inventory.get(match.getMatchIndex());
                                        updateQuantity.setQuantity(updateQuantity.getQuantity() - numItemsToPay);
                                        listOfNumItemsToPay.add(numItemsToPay);
                                    }
                                    else{
                                        System.out.println("Error: Item not found");
                                    }
                                }
                                else{
                                    throw new InputMismatchException("Invalid input");
                                }
                            }
                            catch(InputMismatchException expt){
                                System.out.println(expt.getMessage());
                                scnr.nextLine();
                            }
                            do{
                                System.out.println("Is there another product the customer is purchasing? Type 'n' for no and 'y' for yes");
                                command = scnr.next();
                                if((command.charAt(0) == 'n') && (command.length() == 1) || (command.charAt(0) == 'y') && (command.length() == 1)){
                                    break;
                                }
                                else{
                                    System.out.println("Invalid command");
                                    scnr.nextLine();
                                }
                            }while((command.length() != 1) || (command.charAt(0) != 'n'));
                        }while(command.charAt(0) != 'n');
                        System.out.println("How many bags did the customer purchase?");
                        numOfBags = scnr.nextInt();
                        printReceipt(purchaseList, listOfNumItemsToPay, numOfBags, taxValue, bagValue);
                        purchaseList.clear();
                        listOfNumItemsToPay.clear();
                        do{
                            System.out.println("Will the customer donate money to charity? Type 'n' for no and 'y' for yes");
                            command = scnr.next();
                            if((command.charAt(0) == 'n') && (command.length() == 1) || (command.charAt(0) == 'y') && (command.length() == 1)){
                                break;
                            }
                            else{
                                System.out.println("Invalid command");
                                scnr.nextLine();
                            }
                        }while((command.length() != 1) || (command.charAt(0) != 'n'));
                        if(command.charAt(0) == 'y'){
                            if(randomNum.nextInt(20) == 4){
                                System.out.println("Congrats, the customer won the prize!!!");
                            }
                            else{
                                System.out.println("No prize won, thank you for your donation");
                            }
                        }
                    }
                    else{
                        System.out.println("Error, there are no items in Inventory");
                    }
                }
                else if((command.charAt(0) == 's') && (command.length() == 1)){
                    do{    
                        System.out.println("SubCommands for Settings:");
                        System.out.println("'t' = set Tax value");
                        System.out.println("'b' = set Bag fee");
                        System.out.println("'q' = Exit settings");
                        command = scnr.next();
                        if(command.charAt(0) == 't'){
                            System.out.println("Type the new Tax value in decimals");
                            taxValue = scnr.nextDouble();
                        }
                        else if(command.charAt(0) == 'b'){
                            System.out.println("Type the new bag fee value in decimals");
                            bagValue = scnr.nextDouble();
                        }
                        else if(command.charAt(0) == 'q'){
                            
                        }
                    }while(command.charAt(0) != 'q');
                }
                else if((command.charAt(0) == 'q') && (command.length() == 1)){
                    
                }
                else{
                    System.out.println("Invalid Command");
                }
                System.out.println("Commands:");
                System.out.println("'i' = Inventory");
                System.out.println("'p' = Payment");
                System.out.println("'s' = Settings");
                System.out.println("'q' = Exit");
                command = scnr.next();
            }while((command.charAt(0) != 'q') || (command.length() != 1));
        }
        System.out.println("GoodBye");
        scnr.close();
    }
    public static void removeProduct(String productToRemove, ArrayList<product> editInventory){
        int i;
        String compareName;
        product compareObj;

        for(i = 0; i < editInventory.size(); ++i){
            compareObj = editInventory.get(i);
            compareName = compareObj.getName();
            if(compareName.equals(productToRemove)){
                editInventory.remove(i);
                break;
            }
            else{
                continue;
            }
        }
    }
    public static void showInventory(ArrayList<product> showInventory){
        product printProduct;
        int i;

        for(i = 0; i < showInventory.size(); ++i){
            printProduct = showInventory.get(i);
            printProduct.printProduct();
        }
    }
    public static void addProduct(product productToAdd, ArrayList<product> Inventory){
        int i;
        product productSelected;
        String nameToCompare;
        int ii;
        String nameToAdd;
        boolean finishLoop = false;
        String smallerName;

        if(Inventory.size() == 0){
            Inventory.add(productToAdd);
        }
        else{
            nameToAdd = productToAdd.getName();
            for(i = 0; i < Inventory.size(); ++i){
                productSelected = Inventory.get(i);
                nameToCompare = productSelected.getName();
                if(nameToAdd.charAt(0) == nameToCompare.charAt(0)){   
                    if(nameToAdd.length() <= nameToCompare.length()){
                        smallerName = nameToAdd;
                    }
                    else{
                        smallerName = nameToCompare;
                    }
                    for(ii = 0; ii < smallerName.length(); ++ii){
                        if(nameToAdd.charAt(ii) < nameToCompare.charAt(ii)){
                            Inventory.add(i, productToAdd);
                            finishLoop = true;
                            break;
                        }
                        else if(nameToAdd.charAt(ii) > nameToCompare.charAt(ii)){
                            Inventory.add(i + 1, productToAdd);
                            finishLoop = true;
                            break;
                        }
                        else{
                            continue;
                        }
                    }
                }
                else if(nameToAdd.charAt(0) < nameToCompare.charAt(0)){
                    Inventory.add(i, productToAdd);
                    finishLoop = true;
                }
                else{

                }
                if(finishLoop){
                    break;
                }
            }
            if(!finishLoop){
                Inventory.add(productToAdd);
            }
        }
    }
    public static Location checkInventory(String nameToCompare, ArrayList<product> Inventory){
        int i;
        String selectedName;
        product selectedProduct;
        boolean isMatch = false;
        int index = -1;

        for(i = 0; i < Inventory.size(); ++i){
            selectedProduct = Inventory.get(i);
            selectedName = selectedProduct.getName();

            if(nameToCompare.equalsIgnoreCase(selectedName)){
                isMatch = true;
                index = i;
                break;
            }
            else{
                continue;
            }
        }
        Location match = new Location();
        match.setMatch(isMatch);
        match.setMatchIndex(index);
        return match;
    }
    public static void editName(String newName, ArrayList<product> Inventory, Location match){
        product newProduct = new product();
        product copyProduct;

        copyProduct = Inventory.get(match.getMatchIndex());
        newProduct.setName(newName);
        newProduct.setPrice(copyProduct.getPrice());
        newProduct.setDiscount(copyProduct.getDiscount());
        newProduct.setLocation(copyProduct.getLocation());
        newProduct.setQuantity(copyProduct.getQuantity());

        removeProduct(copyProduct.getName(), Inventory);
        addProduct(newProduct, Inventory);
    }
    public static void editPrice(double newPrice, ArrayList<product> Inventory, Location match){
        product editProduct;

        editProduct = Inventory.get(match.getMatchIndex());
        editProduct.setPrice(newPrice);
    }
    public static void editDiscount(double newDiscount, ArrayList<product> Inventory, Location match){
        product editProduct;

        editProduct = Inventory.get(match.getMatchIndex());
        editProduct.setDiscount(newDiscount);
    }
    public static void editLocation(String newLocation, ArrayList<product> Inventory, Location match){
        product editProduct;

        editProduct = Inventory.get(match.getMatchIndex());
        editProduct.setLocation(newLocation);
    }
    public static void editQuantity(int newQuantity, ArrayList<product> Inventory, Location match){
        product editProduct;

        editProduct = Inventory.get(match.getMatchIndex());
        editProduct.setQuantity(newQuantity);
    }
    public static void printReceipt(ArrayList<product> purchasedList, ArrayList<Integer> numItemsPurchased, int numOfBags, double taxValue, double bagValue){
        int i;
        product selectedProduct;
        double subtotal;
        double total = 0.0;

        System.out.println("Receipt:");
        for(i = 0; i < purchasedList.size(); ++i){
            selectedProduct = purchasedList.get(i);
            subtotal = numItemsPurchased.get(i) * (selectedProduct.getPrice() - (selectedProduct.getPrice() * selectedProduct.getDiscount()));
            System.out.print(numItemsPurchased.get(i) + "x " + selectedProduct.getName() + " - $");
            System.out.printf("%.2f",subtotal);
            System.out.println();
            total += subtotal;
        }
        System.out.println();
        System.out.print("Total Taxes: $");
        System.out.printf("%.2f",(taxValue * total));
        System.out.println();
        System.out.print("Total bag fee: $");
        System.out.printf("%.2f", (bagValue * numOfBags));
        System.out.println();
        System.out.print("Total: $");
        System.out.printf("%.2f", (total + (taxValue * total) + (bagValue * numOfBags)));
        System.out.println("\n");
    }
}