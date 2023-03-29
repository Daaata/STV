package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class LatLongTest {
    public double lat, lon;
    public LatLong latlong;

    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{{0,0},{-1,0},{0,-1},{-1,-1},{1,0},{0,1},{1,1},{-1,1},{1,-1}});
    }

    public LatLongTest(double la, double lo) {
        this.lat = la;
        this.lon = lo;
        this.latlong = new LatLong(la,lo);
    }

    @Test
    public void getLat() throws Exception {
        assertEquals(lat,latlong.getLat(),0.001);
    }

    @Test
    public void getLon() throws Exception {
        assertEquals(lon,latlong.getLon(),0.001);
    }

    @Test
    public void add() throws Exception {
        latlong = latlong.add(lon,lat);
        assertEquals(lat+lon,latlong.getLat(),0.001);
        assertEquals(lon+lat,latlong.getLon(),0.001);
    }

    @Test
    public void getString() throws Exception {
        String text = latlong.toString();
        assertEquals("LatLong [lat="+lat+", lon="+lon+"]", text);
    }
}

/* // Lab 1
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
 */