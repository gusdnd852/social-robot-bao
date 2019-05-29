package com.welfarerobotics.welfareapplcation.bot.brain.chat.named_entity;

import com.welfarerobotics.welfareapplcation.bot.brain.chat.crawler.ModelApi;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author : Hyunwoong
 * @when : 5/27/2019 3:16 PM
 * @homepage : https://github.com/gusdnd852
 */
public class RestaurentEntityRecognizer {

    public static List<String> recognize(String preprocessedSpeech) throws IOException {
        String[][] entity = ModelApi.getEntity(preprocessedSpeech, "restaurant");
        String[] kewordGroup = entity[0];
        String[] entityGroup = entity[1];
        List<String> loc = new ArrayList<>();

        for (int i = 0; i < entityGroup.length; i++) {
            if (entityGroup[i].contains("LOCATION")) {
                loc.add(kewordGroup[i]);
            }
        }
        return loc;
    }

}