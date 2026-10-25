/* STM32 按键控制 LED：按一下按键，LED 翻转一次（下降沿检测）。
 * 仿真接线：LED 接 PA5，按键接 PC13（按下为低电平）。
 * 在 Wokwi 等支持 STM32 的在线仿真里运行，无需硬件。
 */
#include "stm32f1xx_hal.h"

static void SystemClock_Config(void);
static void MX_GPIO_Init(void);

int main(void)
{
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();

    GPIO_PinState prev = GPIO_PIN_SET; /* 上一次按键状态，初始为松开 */

    while (1)
    {
        GPIO_PinState now = HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_13);
        if (prev == GPIO_PIN_SET && now == GPIO_PIN_RESET)
        {
            /* 检测到下降沿：按键刚刚按下，翻转 LED */
            HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
            HAL_Delay(20); /* 简单消抖 */
        }
        prev = now;
    }
}

static void MX_GPIO_Init(void)
{
    __HAL_RCC_GPIOA_CLK_ENABLE();
    __HAL_RCC_GPIOC_CLK_ENABLE();

    GPIO_InitTypeDef gpio = {0};
    gpio.Pin = GPIO_PIN_5;
    gpio.Mode = GPIO_MODE_OUTPUT_PP;
    gpio.Pull = GPIO_NOPULL;
    gpio.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init(GPIOA, &gpio);

    gpio.Pin = GPIO_PIN_13;
    gpio.Mode = GPIO_MODE_INPUT;
    gpio.Pull = GPIO_PULLUP;
    HAL_GPIO_Init(GPIOC, &gpio);
}

static void SystemClock_Config(void)
{
    /* 由 CubeMX 生成的时钟配置替代此处，仿真默认时钟即可运行本例 */
}
