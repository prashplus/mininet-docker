#!/bin/bash
# Test script to verify mininet demos

echo "Testing Mininet Docker Setup..."
echo "================================"

# Test 1: Check if mininet is available
echo "Test 1: Checking Mininet installation..."
if command -v mn &> /dev/null; then
    echo "✓ Mininet is installed"
else
    echo "✗ Mininet not found"
    exit 1
fi

# Test 2: Check if OVS is running
echo "Test 2: Checking Open vSwitch..."
if systemctl is-active --quiet openvswitch-switch; then
    echo "✓ Open vSwitch is running"
else
    echo "⚠ Open vSwitch not running, starting..."
    service openvswitch-switch start
fi

# Test 3: Test basic mininet functionality
echo "Test 3: Testing basic Mininet functionality..."
timeout 30 mn --test pingall > /tmp/mn_test.log 2>&1
if grep -q "Results:" /tmp/mn_test.log; then
    echo "✓ Basic Mininet test passed"
else
    echo "✗ Basic Mininet test failed"
    cat /tmp/mn_test.log
fi

# Test 4: Check demo scripts
echo "Test 4: Checking demo scripts..."
demo_count=$(find /root/demos -name "*.py" | wc -l)
if [ $demo_count -ge 5 ]; then
    echo "✓ Found $demo_count demo scripts"
else
    echo "✗ Expected at least 5 demo scripts, found $demo_count"
fi

# Test 5: Check Python dependencies
echo "Test 5: Checking Python dependencies..."
python3 -c "import mininet.net; print('✓ Mininet Python module available')" 2>/dev/null || echo "✗ Mininet Python module not available"

echo "================================"
echo "Test completed!"
echo ""
echo "To run demos:"
echo "  python3 /root/demos/simple_topology.py"
echo "  python3 /root/demos/webserver_demo.py"
echo "  python3 /root/demos/performance_test.py"
echo ""
echo "To start interactive mininet:"
echo "  mn"
