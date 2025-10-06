package com.rslakra.swaggerservice.enums;

import java.util.EnumSet;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Rohtash Lakra
 * @version 1.0.0
 * @since Aug 08, 2021 15:49:10
 */
public enum Week {
    SUNDAY(0),
    MONDAY(1),
    TUESDAY(2),
    WEDNESDAY(3),
    THURSDAY(4),
    FRIDAY(5),
    SATURDAY(6);
    
    private static final Map<Integer, Week> WEEK_LOOKUP = new HashMap<>();
    
    private int code;
    
    Week(int code) {
        this.code = code;
    }
    
    public int getCode() {
        return code;
    }
    
    /**
     * @param code
     * @return
     */
    public static Week get(int code) {
        if (WEEK_LOOKUP.isEmpty()) {
            EnumSet.allOf(Week.class).forEach(week -> WEEK_LOOKUP.put(week.getCode(), week));
        }
        
        return WEEK_LOOKUP.get(code);
    }
}
