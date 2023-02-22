package com.example.demopgms;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @Autowired //TestService ts = new TestService();
    TestService ts;

//    public TestController(TestService ts) {
//        this.ts = ts;
//    }

    @RequestMapping(value = "/test", method = RequestMethod.GET)
    public String test() {
        return ts.test();
    }

    @RequestMapping("/apple")
    public String apple() {
        return "apple";
    }

    @RequestMapping(value = "/save")
    public String save(@RequestParam("value") String value) {
        return ts.save(value);
//        return value; //확인
    }

    @RequestMapping(value = "/search")
    public String search(@RequestParam("id") Long id) {
        return ts.search(id);
    }
}
