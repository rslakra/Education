package com.rslakra.libraryclient.entity;

import com.rslakra.appsuite.spring.payload.dto.NamedEntityDTO;
import com.rslakra.libraryclient.controller.EntityStatus;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serializable;

/**
 * @author Rohtash Lakra
 * @created 8/20/21 7:11 PM
 */
@Getter
@Setter
@NoArgsConstructor
public class Role extends NamedEntityDTO implements Serializable {

    private EntityStatus status = EntityStatus.INACTIVE;

}
