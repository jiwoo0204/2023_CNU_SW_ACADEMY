package com.example.demopgms;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TestService {

    @Autowired //TestService ts = new TestService();
    TestRepository tr;

    public String test() {
        return tr.test();
    }

    public String save(String value) {
        return tr.save(value);
    }

    public String search(Long id) {
        return tr.search(id);
    }
}
