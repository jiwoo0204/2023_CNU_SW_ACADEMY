package com.example.demopgms;

import org.springframework.stereotype.Repository;

import java.util.HashMap;
import java.util.Map;

@Repository
public class TestRepository {

    Map<Long, String> db = new HashMap<>();
    Long id = 1L;

    // 자바 컬렉션 중 2개 -> list, map만 알면 된다.

    /*
     * 1. DB에 데이터를 삽입하는 메소드 save (1, "test")
     * 2. test() 메소드 -> key값 1을 가지고 db에서 "test" value 찾아서 반환 (return 자리)
     */

    public String save(String value) {
        db.put(id++, value);
        return value;
    }

    public String test() {
        //DB에서 받아와 리턴
        return db.get(id);
    }

    public String search(Long id) {
        return db.get(id);
    }
}
