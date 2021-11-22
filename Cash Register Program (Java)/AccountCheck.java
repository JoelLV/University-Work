public class AccountCheck {
    public static boolean correctAccount(String username, String password){
        String keyUsername = "JoelLV";
        String keyPassword = "1234";
        boolean pass = true;

        if(username.equals(keyUsername) && (password.equals(keyPassword))){
            return pass;
        }
        else{
            pass = false;
            return pass;
        }
    }
}