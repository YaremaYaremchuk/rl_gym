# Reinforcement Learning (RL) model from scratch, trained using the OpenAI Gym Mountain Car environment🤖
<img width="635" alt="size_20" src="https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/f8f147b8-23a7-4e43-ae77-7aeee5cef0b1"> <br><br>
## Observation Size Importance❗️
Experimented with observation sizes of 20, 40, and 80. <br><br>
<img width="635" alt="size_20" src="https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/93300446-8846-4a16-8538-bb90abb99f5f"> <br><br>
Size 20: After 13,000 episodes, the model hit the ceiling and overfitted to the best routes, leading to performance drops in varied environments. <br><br>
<img width="635" alt="size_80" src="https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/909b41ef-f2ad-4809-8046-1a6aebd7dd2f"><br><br>
Size 80: Required twice as many episodes and significant training time. The model remained unstable with a jumpy performance graph. <br><br>
<img width="635" alt="size_40" src="https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/a1213246-bc22-4f62-973d-013106c79a82"><br><br>
Size 40: Struck the optimal balance. Provided more values for better performance than size 20 and was more stable than size 80, achieving consistent good results.
<br><br>
## Q-Table Progression📈
- Early Q-table:
<br><br>
![0](https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/c4e8b9fd-bca9-42a1-9ce2-392e0de5e616)
<br><br>
- Final Q-table:
<br><br>
![24990](https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/575cdeca-0d42-40c1-b049-21db1e647aa4)
<br><br>
- Video:

https://github.com/YaremaYaremchuk/rl_gym/assets/89141796/763b3b21-bb64-4832-8b3a-dd77bce27888



Early Q-tables are random, but as the model explores, it updates values to reflect optimal actions (white action is action with the best reward).

As we can see, when the cart has negative velocity (y-axis < 20): Best action is 0 (move left). <br>
Positive velocity: Best action is 2 (move right). <br>
This strategy helps the car gain momentum to climb the mountain to the top.

## Role of Epsilon "ε"

Epsilon was crucial in randomizing initial decisions, allowing the model to explore diverse action combinations and avoid overfitting.

## Conclusion🎬

It was thrilling to witness the model successfully climb the hill for the first time, demonstrating the power and potential of reinforcement learning.
Explore the repository to see detailed graphs, code implementation, and a video of the model's Q-table progression.
