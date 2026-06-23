package com.revature;

import io.javalin.Javalin;
import com.revature.controllers.AuthController;

public class Main {
    public static void main(String[] args) {
        AuthController authController = new AuthController();

        Javalin app = Javalin.create(config -> {
            config.routes.post("/login", authController.loginHandler);
        });

        app.start(8080);
    }
}