//
// Created by todd on 2/10/21.
//

#ifndef AIMI_CONTROLLERS_H
#define AIMI_CONTROLLERS_H


class controllers {
private:
    bool real_hardware;
    double current_position_xyz[3]; //X, Y, Z
    double current_position_theta[4]; //theta0..theta2, altitude
public:
    controllers(bool hardware);
    double* getCurrentPositionXYZ() {return current_position_xyz;}
    double* getCurrentPositionTheta() {return current_position_theta;}
    double* goToXYZ(double x, double y, double z);
    double* goToTheta(double theta0, double theta1, double theta2, double altitude);
    void click(double targetX, double targetY);
    void drag(double startX, double startY, double dx, double dy, double duration);
};


#endif //AIMI_CONTROLLERS_H
