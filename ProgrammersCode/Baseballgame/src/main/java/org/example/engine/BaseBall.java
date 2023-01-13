package org.example.engine;

import lombok.AllArgsConstructor;
import org.example.engine.io.Input;
import org.example.engine.io.NumberGenerator;
import org.example.engine.io.Output;
import org.example.engine.model.BallCount;
import org.example.engine.model.Numbers;

import java.util.Optional;
import java.util.concurrent.atomic.AtomicInteger;

@AllArgsConstructor
public class BaseBall implements Runnable {
    private final int COUNT_OF_NUMBERS = 3;

    private NumberGenerator generator;
    private Input input;
    private Output output;

    @Override
    public void run() {
        Numbers answer = generator.generate(COUNT_OF_NUMBERS);
        while (true) {
            String inputString = input.input("숫자를 맞춰보세요. : ");
            Optional<Numbers> inputNumbers = parse(inputString);
            if (inputNumbers.isEmpty()) {
                output.inputError();
                continue;
            }

            BallCount bc = ballCount(answer, inputNumbers.get());
            output.ballcount(bc);
            if (bc.getStrike() == COUNT_OF_NUMBERS) {
                output.correct();
                break;
            }
        }
    }

    private BallCount ballCount(Numbers answer, Numbers inputNumbers) {
        //동기화
        AtomicInteger strike = new AtomicInteger();
        AtomicInteger ball = new AtomicInteger();

        answer.indexedForEach((a, i) -> {
            inputNumbers.indexedForEach((n, j) -> {
                //동일한 값이 있는지, 있다면 인덱스도 같은지 확인
                if (!a.equals(n)) return;
                if (i.equals(j)) strike.addAndGet(1);
                else ball.addAndGet(1);
            });
        });

        return new BallCount(strike.get(), ball.get());
    }

    private Optional<Numbers> parse(String inputString) {
        if (inputString.length() != COUNT_OF_NUMBERS) return Optional.empty();

        long count = inputString.chars()
                .filter(Character::isDigit) //영문자 제거
                .map(Character::getNumericValue)
                .filter(i -> i > 0)
                .distinct()
                .count();

        if (count != COUNT_OF_NUMBERS) return Optional.empty();
        return Optional.of( //감싸서 리턴
                new Numbers( //Numbers 객체로 생성하여
                        inputString.chars()
                                .map(Character::getNumericValue)
                                .boxed()
                                .toArray(Integer[]::new) //배열 변환
                )
        );
    }
}
