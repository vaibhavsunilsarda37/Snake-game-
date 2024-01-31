import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.advanced.AdvancedPlayer;
import javazoom.jl.player.advanced.PlaybackEvent;
import javazoom.jl.player.advanced.PlaybackListener;

public class MusicPlayer extends JFrame {
    private JButton playButton, stopButton;
    private AdvancedPlayer player;
    private Thread playerThread;

    public MusicPlayer() {
        setTitle("Simple Music Player");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 100);

        playButton = new JButton("Play");
        stopButton = new JButton("Stop");

        playButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                play();
            }
        });

        stopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                stop();
            }
        });

        JPanel panel = new JPanel();
        panel.add(playButton);
        panel.add(stopButton);
        add(panel);

        setVisible(true);
    }

    private void play() {
        if (player == null || player.isComplete()) {
            File file = new File("path/to/your/music.mp3"); // Replace with the path to your music file
            try {
                player = new AdvancedPlayer(getClass().getResourceAsStream(file.getPath()), javazoom.jl.player.FactoryRegistry.systemRegistry().createAudioDevice());
                playerThread = new Thread(() -> {
                    try {
                        player.play(0, Integer.MAX_VALUE);
                    } catch (JavaLayerException e) {
                        e.printStackTrace();
                    }
                });
                playerThread.start();
            } catch (JavaLayerException e) {
                e.printStackTrace();
            }
        }
    }

    private void stop() {
        if (player != null) {
            player.close();
            playerThread.interrupt();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new MusicPlayer());
    }
}