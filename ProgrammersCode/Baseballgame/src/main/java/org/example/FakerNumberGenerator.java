package org.example;

import com.github.javafaker.Faker;
import org.example.engine.io.NumberGenerator;
import org.example.engine.model.Numbers;

import java.util.stream.Stream;

public class FakerNumberGenerator implements NumberGenerator {
    private final Faker faker = new Faker();
    @Override
    public Numbers generate(int count) {
        Numbers nums =  new Numbers(
                Stream.generate(() -> faker.number().randomDigitNotZero())
                        .limit(count)
                        .toArray(Integer[]::new)
        );
        System.out.println(nums);
        return nums;
    }
}
