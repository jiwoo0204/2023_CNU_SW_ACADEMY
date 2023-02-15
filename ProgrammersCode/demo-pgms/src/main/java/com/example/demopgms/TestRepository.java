package com.example.demopgms;

import org.springframework.stereotype.Repository;

import java.util.HashMap;
import java.util.Map;

@Repository
public class TestRepository {
    //private Map<String, String> db = new HashMap<>();
    // 자바 컬렉션 중 2개 -> list, map만 알면 된다.
    public String test() {
        //DB에서 받아와 리턴
        return "test";
    }
}
