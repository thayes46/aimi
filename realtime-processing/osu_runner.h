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
 * Use openCV to
 * @return 0 if successful, nonzero otherwise
 */
int findTargets();
/**
 * Use the controller from firmware to be able to send movement commands
 */
void clickTarget();

#endif //AIMI_OSU_RUNNER_H
