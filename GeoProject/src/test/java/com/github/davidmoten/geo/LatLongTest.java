package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class LatLongTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void TestLatLong() throws Exception {
        LatLong ll = new LatLong(1,1);
    }

    @Test
    public void getLatAndLon() throws Exception {
        LatLong ll = new LatLong(3,6);
        ll = ll.add(3,3);
        double lat = ll.getLat();
        double lon = ll.getLon();
        assertEquals(6,lat,0.001);
        assertEquals(9,lon,0.001);
    }

    @Test
    public void TesttoString() throws Exception {
        double lat = 3;
        double lon = 6;
        LatLong ll = new LatLong(lat, lon);
        String line = ll.toString();
        assertEquals("LatLong [lat="+lat+", lon="+lon+"]", line);
    }

}