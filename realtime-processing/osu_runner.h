//
// Created by todd on 2/10/21.
//

#ifndef AIMI_OSU_RUNNER_H
#define AIMI_OSU_RUNNER_H
#include <mutex>
#include <opencv2/opencv.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <thread>

CvMat FRAME_BUFFER[120];
std::mutex FRAME_MUTEX;



void readStream();
void selectFrame();
/**
 * Use openCV to find current position as well as the targeted position
 * in osu current is cursor in valorant current is enemy head/target
 * in osu target is center of circle, in valorant, target is crosshair
 * @return 0 if successful, nonzero otherwise
 */
int findTargets();
/**
 * Use the controller from firmware to be able to send movement commands
 */
void clickTarget();

#endif //AIMI_OSU_RUNNER_H
