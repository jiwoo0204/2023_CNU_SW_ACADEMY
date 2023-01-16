package org.example;

import org.example.engine.BaseBall;
import org.example.engine.io.Input;
import org.example.engine.io.NumberGenerator;
import org.example.engine.io.Output;

public class App {
    public static void main(String[] args) {

        NumberGenerator generator = new FakerNumberGenerator();
        Console console = new Console();

        new BaseBall(generator, console, console).run();
    }
}
