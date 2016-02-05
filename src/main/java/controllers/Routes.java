package controllers;

import spark.ModelAndView;

import java.util.HashMap;
import java.util.Map;

import static spark.Spark.get;
/**
 * Created by dylan on 2/5/16.
 */
public class Routes {
    public static void main(String[] args) {
        get("/hello", (req, res) -> "Hello World");


        get("/index", (req, res) -> {
            Map<String, String> map = new HashMap<>();
            map.put("title", "Catshark");

           return new ModelAndView(map, "index.hbs");
        }, new HandlebarsTemplateEngine()); // load the handlebars tempalte engine to render the page

    }
}
