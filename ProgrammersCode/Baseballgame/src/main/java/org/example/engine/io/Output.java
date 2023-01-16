package org.example.engine.io;

import org.example.engine.model.BallCount;

public interface Output {
    void ballcount(BallCount bc);

    void inputError();

    void correct();
}
