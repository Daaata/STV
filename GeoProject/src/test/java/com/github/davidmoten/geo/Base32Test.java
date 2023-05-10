package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.*;

public class Base32Test {

    @Test
    public void encodeBase32() throws Exception {
        String encode = Base32.encodeBase32(75324, 4);
        assertEquals("29jw", encode);
        encode = Base32.encodeBase32(-75324, 4);
        assertEquals("-29jw", encode);
        encode = Base32.encodeBase32(16, 1);
        assertEquals("h", encode);
        encode = Base32.encodeBase32(-16, 1);
        assertEquals("-h", encode);
        encode = Base32.encodeBase32(75324, 8);
        assertEquals("000029jw", encode);
        encode = Base32.encodeBase32(-75324, 8);
        assertEquals("-000029jw", encode);
        encode = Base32.encodeBase32(75324);
        assertEquals("0000000029jw", encode);
        encode = Base32.encodeBase32(-75324);
        assertEquals("-0000000029jw", encode);
    }

    @Test
    public void decodeBase32() throws Exception {
        long decode = Base32.decodeBase32("29jw");
        assertEquals(75324, decode);
        decode = Base32.decodeBase32("-29jw");
        assertEquals(-75324, decode);
        decode = Base32.decodeBase32("");
        assertEquals(0, decode);
    }

    @Test(expected = IllegalArgumentException.class)
    public void getCharIndex() throws Exception {
        assertEquals(0,Base32.getCharIndex('0'));
        Base32.getCharIndex('A');
    }

    @Test
    public void padLeftWithZerosToLength() throws Exception {
        assertEquals("29jw",Base32.padLeftWithZerosToLength("29jw",4));
        assertEquals("029jw",Base32.padLeftWithZerosToLength("29jw",5));
    }
}

/* //Lab 1//
@RunWith(Parameterized.class)
public class Base32Test {


    public long i;
    public int length;
    public String text;

    @Parameterized.Parameters public static Collection<Object[]> parameters() {
        return Arrays.asList(new Object[][] {{75324, 4, "29jw"}, {-75324, 4, "-29jw"}, {null ,4,"000000000004"}});
    }

    public Base32Test(long a, int b, String c){
        this.i = a;
        this.length = b;
        this.text = c;
    }

    @Test
    public void encodeBase32() {
        assertEquals(text, Base32.encodeBase32(i,length));
    }


    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void encodeBase32() throws Exception {
        String encode = Base32.encodeBase32(75324, 4);
        assertEquals("29jw", encode);
        encode = Base32.encodeBase32(-75324, 4);
        assertEquals("-29jw", encode);
        encode = Base32.encodeBase32(4);
        assertEquals("000000000004", encode);
    }

    @Test
    public void decodeBase32() throws Exception {
        long decode = Base32.decodeBase32("29jw");
        assertEquals(75324, decode);
    }

    @Test(expected = IllegalArgumentException.class)
    public void getCharIndex() throws Exception {
        int char_index = Base32.getCharIndex('0');
        assertEquals(0, char_index);
        Base32.getCharIndex('A');
    }

    @Test
    public void padLeftWithZerosToLength() throws Exception {
        String s = Base32.padLeftWithZerosToLength("Lucy",5);
        assertEquals("0Lucy", s);
        s = Base32.padLeftWithZerosToLength("JenJen",6);
        assertEquals("JenJen", s);
    }

}
*/