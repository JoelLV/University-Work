<?php
   function passcheck($username,$password) {
     $adServer = "ldap://ethos.sau.southern.edu";
     $ds = ldap_connect($adServer);
     $ldaprdn = 'sau' . "\\" . $username;
     $ldapbind=false;
     if (ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3)) {
       if (ldap_start_tls($ds)) {
         $ldapbind =  @ldap_bind($ds, $ldaprdn, $password);
       }
     }
     return ($ldapbind)? true : false;
   }
?>