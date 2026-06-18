package com.revature.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/*
This class is where we manage and establish our database connection which
we will use to interact with our database.
*/

public class ConnectionUtil {

    public static Connection getConnection() throws SQLException{

        //first we need to register our SQLite driver
        //this process makes the application aware of what SQL flavor we're using
        try{
            Class.forName("org.sqlite.JDBC"); //searching for the SQLite driver, which we have as a dependency

        }catch (ClassNotFoundException e){
            e.printStackTrace();
            System.out.println("problem occurred locating driver");

        }

        //use this string in a method that gets connections
        String url = "jdbc:sqlite:database/expense_manager.db";

        // returns our actual database Connection object
        return DriverManager.getConnection(url);
    }
}