package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

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